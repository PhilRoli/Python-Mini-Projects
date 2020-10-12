import win10toast as toast

Toaster = toast.ToastNotifier()

Toaster.show_toast('application name', 'your message', duration=10)