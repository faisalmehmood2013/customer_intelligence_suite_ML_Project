"""
main_utils.py
---------------
Common/reusable helper functions - SAB tiers yeh functions use karenge.

Yahan generic functions likhenge jaise:
    - read_yaml_file(path)       -> config/schema.yaml ya model.yaml padhne ke liye
    - write_yaml_file(path, data)
    - save_object(file_path, obj)        -> trained model (.pkl) save karna (joblib/pickle)
    - load_object(file_path)             -> saved model wapis load karna
    - save_numpy_array_data(path, array)  -> processed features save karna
    - load_numpy_array_data(path)

Yeh exact wahi cheezen hain jo har tier (CLV ho ya Churn) ko equally
chahiye hongi - isliye yahan ek hi jagah likhte hain, baar baar nahi.
"""
