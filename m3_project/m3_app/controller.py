from objectpack.observer import Observer, ObservableController

 
observer = Observer()
controller = ObservableController(
    url='actions',
    observer=observer,
)
