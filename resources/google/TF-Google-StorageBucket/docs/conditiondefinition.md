# TF::Google::StorageBucket ConditionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#age" title="Age">Age</a>" : <i>Double</i>,
    "<a href="#createdbefore" title="CreatedBefore">CreatedBefore</a>" : <i>String</i>,
    "<a href="#customtimebefore" title="CustomTimeBefore">CustomTimeBefore</a>" : <i>String</i>,
    "<a href="#dayssincecustomtime" title="DaysSinceCustomTime">DaysSinceCustomTime</a>" : <i>Double</i>,
    "<a href="#dayssincenoncurrenttime" title="DaysSinceNoncurrentTime">DaysSinceNoncurrentTime</a>" : <i>Double</i>,
    "<a href="#matchesstorageclass" title="MatchesStorageClass">MatchesStorageClass</a>" : <i>[ String, ... ]</i>,
    "<a href="#noncurrenttimebefore" title="NoncurrentTimeBefore">NoncurrentTimeBefore</a>" : <i>String</i>,
    "<a href="#numnewerversions" title="NumNewerVersions">NumNewerVersions</a>" : <i>Double</i>,
    "<a href="#withstate" title="WithState">WithState</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#age" title="Age">Age</a>: <i>Double</i>
<a href="#createdbefore" title="CreatedBefore">CreatedBefore</a>: <i>String</i>
<a href="#customtimebefore" title="CustomTimeBefore">CustomTimeBefore</a>: <i>String</i>
<a href="#dayssincecustomtime" title="DaysSinceCustomTime">DaysSinceCustomTime</a>: <i>Double</i>
<a href="#dayssincenoncurrenttime" title="DaysSinceNoncurrentTime">DaysSinceNoncurrentTime</a>: <i>Double</i>
<a href="#matchesstorageclass" title="MatchesStorageClass">MatchesStorageClass</a>: <i>
      - String</i>
<a href="#noncurrenttimebefore" title="NoncurrentTimeBefore">NoncurrentTimeBefore</a>: <i>String</i>
<a href="#numnewerversions" title="NumNewerVersions">NumNewerVersions</a>: <i>Double</i>
<a href="#withstate" title="WithState">WithState</a>: <i>String</i>
</pre>

## Properties

#### Age

Minimum age of an object in days to satisfy this condition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedBefore

A date in the RFC 3339 format YYYY-MM-DD. This condition is satisfied when an object is created before midnight of the specified date in UTC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTimeBefore

A date in the RFC 3339 format YYYY-MM-DD. This condition is satisfied when the customTime metadata for the object is set to an earlier date than the date used in this lifecycle condition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysSinceCustomTime

Days since the date set in the `customTime` metadata for the object. This condition is satisfied when the current date and time is at least the specified number of days after the `customTime`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysSinceNoncurrentTime

Relevant only for versioned objects. Number of days elapsed since the noncurrent timestamp of an object.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchesStorageClass

[Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects to satisfy this condition. Supported values include: `STANDARD`, `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`, `DURABLE_REDUCED_AVAILABILITY`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentTimeBefore

Relevant only for versioned objects. The date in RFC 3339 (e.g. `2017-06-13`) when the object became nonconcurrent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumNewerVersions

Relevant only for versioned objects. The number of newer versions of an object to satisfy this condition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WithState

Match to live and/or archived objects. Unversioned buckets have only live objects. Supported values include: `"LIVE"`, `"ARCHIVED"`, `"ANY"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

