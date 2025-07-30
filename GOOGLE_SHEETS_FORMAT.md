# Google Sheets Format for Fantasy Tour de France App

## Required Structure

Your Google Sheets must have this exact format for the app to read the data correctly:

### Row Layout:

```
Row 1: Headers (can be anything - ignored by app)
Row 2: Stage numbers or labels (ignored by app)
Row 10+: Participant data rows

Participant Row Format:
[Participant Name] | [Stage 1 Time] | [Stage 2 Time] | [Stage 3 Time] | ... | [Stage 21 Time]
```

### Example Format:

```
|     | Jeremy | Leo   | Charles | Aaron | Nate  |        |        |
|-----|--------|-------|---------|-------|-------|--------|--------|
| ... | ...    | ...   | ...     | ...   | ...   | ...    | ...    |
|Stage| 1      | 2     | 3       | 4     | 5     | 6      | 7      |
|Jeremy|0:08:19 |0:10:19|0:10:19  |0:16:41|0:25:39|0:27:15 |0:34:28 |
|Leo   |0:07:06 |0:12:09|0:12:09  |0:20:46|0:27:55|0:29:12 |0:46:58 |
|Charles|0:06:27|0:11:30|0:11:30  |0:18:51|0:26:46|0:29:51 |0:43:41 |
|Aaron |0:01:09 |0:01:40|0:01:40  |0:04:44|0:08:00|0:09:25 |0:12:46 |
|Nate  |0:10:59 |0:16:33|0:16:33  |0:30:18|0:38:37|0:44:16 |1:00:03 |
```

## Critical Requirements:

### 1. Participant Names (Column A)
- Must be exactly: `Jeremy`, `Leo`, `Charles`, `Aaron`, `Nate`
- Case sensitive
- No extra spaces
- Must start around row 10 or later

### 2. Time Format
- Use format: `H:MM:SS` (e.g., `0:08:19`, `1:23:45`)
- Leading zeros required for minutes and seconds
- Use `0:00:00` for stages not yet completed

### 3. Column Structure
- Column A: Participant names
- Columns B through V: Stage times (Stages 1-21)
- App reads up to 22 columns total

### 4. Data Placement
- Participant data should start around row 10
- Earlier rows can contain headers, labels, or other data (ignored)
- App searches for exact participant name matches

## Google Sheets Setup Steps:

1. **Create New Sheet**: Go to sheets.google.com
2. **Set Sharing**: File > Share > "Anyone with the link can view"
3. **Format Data**: Use the structure shown above
4. **Get CSV URL**: Replace `SHEET_ID` in this URL:
   ```
   https://docs.google.com/spreadsheets/d/SHEET_ID/export?format=csv
   ```

## Time Entry Tips:

- **Cumulative Times**: Enter the total race time after each stage
- **Format Consistency**: Always use H:MM:SS format
- **Future Stages**: Use `0:00:00` for stages not completed
- **Updates**: App checks for new data every 5 minutes

## Example Data Entry:

After Stage 5, if Aaron has a total time of 25 minutes and 39 seconds:
- Enter: `0:25:39`
- Not: `25:39` or `0:25:39.0`

The app will automatically calculate rankings and time gaps based on these cumulative times.