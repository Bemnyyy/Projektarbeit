def rename_table(engine):
    with engine.connect() as conn:
        conn.execute(text('ALTER TABLE karlsruhe_weather_3 RENAME TO karlsruhe_weather_11_2025'))
        conn.commit()
    print("Tabelle erfolgreich umbenannt.")

engine = create_engine(f"sqlite:///{DB_PATH}")
rename_table(engine)