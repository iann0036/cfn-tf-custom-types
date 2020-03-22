# Terraform::Alicloud::OtsTable

Provides an OTS table resource.

-> **NOTE:** From Provider version 1.10.0, the provider field 'ots_instance_name' has been deprecated and
you should use resource alicloud_ots_table's new field 'instance_name' and 'table_name' to re-import this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::OtsTable",
    "Properties" : {
        "<a href="#deviationcellversioninsec" title="DeviationCellVersionInSec">DeviationCellVersionInSec</a>" : <i>String</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#maxversion" title="MaxVersion">MaxVersion</a>" : <i>Double</i>,
        "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>,
        "<a href="#timetolive" title="TimeToLive">TimeToLive</a>" : <i>Double</i>,
        "<a href="#primarykey" title="PrimaryKey">PrimaryKey</a>" : <i>[ <a href="primarykey.md">PrimaryKey</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::OtsTable
Properties:
    <a href="#deviationcellversioninsec" title="DeviationCellVersionInSec">DeviationCellVersionInSec</a>: <i>String</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#maxversion" title="MaxVersion">MaxVersion</a>: <i>Double</i>
    <a href="#tablename" title="TableName">TableName</a>: <i>String</i>
    <a href="#timetolive" title="TimeToLive">TimeToLive</a>: <i>Double</i>
    <a href="#primarykey" title="PrimaryKey">PrimaryKey</a>: <i>
      - <a href="primarykey.md">PrimaryKey</a></i>
</pre>

## Properties

#### DeviationCellVersionInSec

The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

The name of the OTS instance in which table will located.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxVersion

The maximum number of versions stored in this table. The valid value is 1-2147483647.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

The table name of the OTS instance. If changed, a new table would be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeToLive

The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryKey

_Required_: No

_Type_: List of <a href="primarykey.md">PrimaryKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

