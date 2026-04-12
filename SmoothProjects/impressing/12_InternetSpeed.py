# pip install speedtest-cli
import speedtest

print("---INITIALIZING SPEED TRACKER---")
st = speedtest.Speedtest()

print(">>Finding best server...")
st.get_best_server()

print(">> Testing Download Speed...")
download = st.download()/1_000_000

print(">> Testing Upload Speed...")
upload = st.upload() / 1_000_000

print(f"\n Results")
print(f"Download: {download:.2f} Mbps")
print(f"Upload: {upload:.2f} Mbps")

print("\n Stay Fast")