# Terraform::Alicloud::OtsTable

CloudFormation equivalent of alicloud_ots_table

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::OtsTable",
    "Properties" : {
        "<a href="#deviationcellversioninsec" title="DeviationCellVersionInSec">DeviationCellVersionInSec</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#maxversion" title="MaxVersion">MaxVersion</a>" : <i>Double</i>,
        "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>,
        "<a href="#timetolive" title="TimeToLive">TimeToLive</a>" : <i>Double</i>,
        "<a href="#primarykey" title="PrimaryKey">PrimaryKey</a>" : <i>[ &lt;a href=&#34;primarykey.md&#34;&gt;PrimaryKey&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::OtsTable
Properties:
    <a href="#deviationcellversioninsec" title="DeviationCellVersionInSec">DeviationCellVersionInSec</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#maxversion" title="MaxVersion">MaxVersion</a>: <i>Double</i>
    <a href="#tablename" title="TableName">TableName</a>: <i>String</i>
    <a href="#timetolive" title="TimeToLive">TimeToLive</a>: <i>Double</i>
    <a href="#primarykey" title="PrimaryKey">PrimaryKey</a>: <i>
      - &lt;a href=&#34;primarykey.md&#34;&gt;PrimaryKey&lt;/a&gt;</i>
</pre>

## Properties

#### DeviationCellVersionInSec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxVersion

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeToLive

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryKey

_Required_: No

_Type_: List of &lt;a href=&#34;primarykey.md&#34;&gt;PrimaryKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

