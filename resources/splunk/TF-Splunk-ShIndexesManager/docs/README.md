# TF::Splunk::ShIndexesManager

Create indexes on Splunk Cloud instances. [BETA]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::ShIndexesManager",
    "Properties" : {
        "<a href="#datatype" title="Datatype">Datatype</a>" : <i>String</i>,
        "<a href="#frozentimeperiodinsecs" title="FrozenTimePeriodInSecs">FrozenTimePeriodInSecs</a>" : <i>String</i>,
        "<a href="#maxglobalrawdatasizemb" title="MaxGlobalRawDataSizeMb">MaxGlobalRawDataSizeMb</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ <a href="acldefinition.md">AclDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::ShIndexesManager
Properties:
    <a href="#datatype" title="Datatype">Datatype</a>: <i>String</i>
    <a href="#frozentimeperiodinsecs" title="FrozenTimePeriodInSecs">FrozenTimePeriodInSecs</a>: <i>String</i>
    <a href="#maxglobalrawdatasizemb" title="MaxGlobalRawDataSizeMb">MaxGlobalRawDataSizeMb</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - <a href="acldefinition.md">AclDefinition</a></i>
</pre>

## Properties

#### Datatype

Valid values: (event | metric). Specifies the type of index.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrozenTimePeriodInSecs

Number of seconds after which indexed data rolls to frozen.
Defaults to 94608000 (3 years).Freezing data means it is removed from the index. If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxGlobalRawDataSizeMb

The maximum size of an index (in MB). If an index grows larger than the maximum size, the oldest data is frozen.
Defaults to 100 MB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the index to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: List of <a href="acldefinition.md">AclDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

