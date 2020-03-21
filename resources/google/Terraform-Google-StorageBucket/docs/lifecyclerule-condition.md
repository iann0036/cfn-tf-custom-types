# Terraform::Google::StorageBucket LifecycleRule Condition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#age" title="Age">Age</a>" : <i>Double</i>,
    "<a href="#createdbefore" title="CreatedBefore">CreatedBefore</a>" : <i>String</i>,
    "<a href="#islive" title="IsLive">IsLive</a>" : <i>Boolean</i>,
    "<a href="#matchesstorageclass" title="MatchesStorageClass">MatchesStorageClass</a>" : <i>[ String, ... ]</i>,
    "<a href="#numnewerversions" title="NumNewerVersions">NumNewerVersions</a>" : <i>Double</i>,
    "<a href="#withstate" title="WithState">WithState</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#age" title="Age">Age</a>: <i>Double</i>
<a href="#createdbefore" title="CreatedBefore">CreatedBefore</a>: <i>String</i>
<a href="#islive" title="IsLive">IsLive</a>: <i>Boolean</i>
<a href="#matchesstorageclass" title="MatchesStorageClass">MatchesStorageClass</a>: <i>
      - String</i>
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

Creation date of an object in RFC 3339 (e.g. `2017-06-13`) to satisfy this condition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsLive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchesStorageClass

[Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects to satisfy this condition. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `STANDARD`, `DURABLE_REDUCED_AVAILABILITY`.

_Required_: No

_Type_: List of String

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

