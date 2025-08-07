class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(),0)
    
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        iter(self.tags)

        

cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
len(cloud)
cloud["python"] = 10
