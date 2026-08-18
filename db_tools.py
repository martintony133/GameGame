import os
import sys
import django
import psycopg2

# 1. 自動初始化 Django 環境（這樣就能直接讀取 Django 的設定與 Model）
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.conf import settings
from django.apps import apps

def get_db_connection():
    db_config = settings.DATABASES['default']
    return psycopg2.connect(
        dbname = "gamegame",
        user = "postgres",
        password = "950256",
        host = "localhost",
        port = "5432"
)

def get_table_name(model_name):
    """自動根據 Model 名稱找出 PostgreSQL 的 Table 名稱"""
    try:
        # 自動搜尋整個專案，只要 Model 名字對了就抓出來
        model = apps.get_model(model_name)
        return model._meta.db_table
    except LookupError:
        # 如果找不到，就嘗試尋找特定 app 裡面的 model
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                return model._meta.db_table
            except LookupError:
                continue
    return None

def main():
    if len(sys.argv) < 3:
        print("\n❌ 使用方法錯誤！請輸入指令、Model名稱與檔案路徑。")
        print("格式: python db_tools.py [export/import] [Model名稱] [CSV檔案名稱]")
        print("範例: python db_tools.py export game output.csv\n")
        return

    action = sys.argv[1].lower()     # export 或 import
    target_model = sys.argv[2]       # 例如: game
    file_path = sys.argv[3]          # 例如: data.csv

    # 自動獲取 Table 名稱，不用手動打
    table_name = get_table_name(target_model)
    if not table_name:
        print(f"❌ 找不到名為 '{target_model}' 的 Django Model，請檢查大小寫是否正確！")
        return

    print(f"🔄 正在連線資料庫，目標 Table: {table_name}...")
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        if action == "export":
            with open(file_path, "w", encoding="utf-8") as f:
                sql = f"COPY {table_name} TO STDOUT WITH CSV HEADER"
                cur.copy_expert(sql, f)
            print(f"✅ 匯出成功！檔案已儲存至: {file_path}")
            # 2. 💡 新增：自動把 Django 的 media 圖片資料夾複製一份到 CSV 旁邊
            try:
                import shutil
                # 假設你的 Django 圖片都存在專案根目錄的 'media' 資料夾
                shutil.copytree('media', f"{file_path}_media", dirs_exist_ok=True)
                print(f"📦 圖片資料夾已同步備份至: {file_path}_media")
            except Exception as e:
                print(f"⚠️ 圖片備份失敗 (可能沒有 media 資料夾): {e}")

        elif action == "import":
            with open(file_path, "r", encoding="utf-8") as f:
                sql = f"COPY {table_name} FROM STDOUT WITH CSV HEADER"
                cur.copy_expert(sql, f)
            conn.commit()
            print(f"✅ 匯入成功！已將 {file_path} 的資料寫入 {table_name}")

            try:
                import shutil
                if os.path.exists(f"{file_path}_media"):
                    shutil.copytree(f"{file_path}_media", 'media', dirs_exist_ok=True)
                    print(f"📂 圖片檔案已自動還原至專案的 'media' 資料夾！")
                else:
                    print(f"💡 提示：找不到對應的圖片備份資料夾 {file_path}_media，請手動檢查圖片。")
            except Exception as e:
                print(f"⚠️ 圖片還原失敗: {e}")
            # 自動修正 PostgreSQL 流水號計數器
            app_label = apps.get_model(target_model)._meta.app_label
            print(f"💡 提示: 匯入完成後，建議執行以下指令同步流水號:")
            print(f"   python manage.py sqlsequencereset {app_label} | python manage.py dbshell")

        else:
            print("❌ 未知的動作！請使用 'export' 或 'import'。")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"💥 發生錯誤: {e}")

if __name__ == "__main__":
    main()