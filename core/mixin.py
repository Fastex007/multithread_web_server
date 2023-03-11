import concurrent


class ThreadPoolMixin:
    pool_size = 1

    def _handle(self, *args, **kwargs) -> None:
        try:
            future = self.__pool.submit(super()._handle, *args, **kwargs)
            self.__futures.append(future)
        except AttributeError:
            self.__pool = concurrent.futures.ThreadPoolExecutor(self.pool_size)
            self.__futures = []
            future = self.__pool.submit(super()._handle, *args, **kwargs)
            self.__futures.append(future)

    def _cleanup(self) -> None:
        try:
            for future in self.__futures:
                future.cancel()

            self.__pool.shutdown()
        except AttributeError:
            pass
