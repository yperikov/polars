import polars as pl

l = b"x\n".join(["h"] + [str(i) for i in range(1,20)])


r = pl.scan_csv(b"x\n" * 20, n_rows=5).head(10).collect().height
r2 = pl.scan_csv(b"x\n" * 20, n_rows=5).head(10).collect(optimizations=pl.QueryOptFlags(slice_pushdown=False)).height

print(r) 
print(r2) 