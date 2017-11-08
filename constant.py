network_chunk_size = 6
check_length_size = 524288000 #500 mb


def _make_timeout_reader(file_like):
    def timeout_reader():
        #with ChunkReadTimeout(self.client_timeout):
        return file_like.read(network_chunk_size)
    return timeout_reader

