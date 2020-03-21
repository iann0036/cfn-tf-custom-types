# Terraform::TencentCloud::Instance DataDisks

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datadiskid" title="DataDiskId">DataDiskId</a>" : <i>String</i>,
    "<a href="#datadisksize" title="DataDiskSize">DataDiskSize</a>" : <i>Double</i>,
    "<a href="#datadisktype" title="DataDiskType">DataDiskType</a>" : <i>String</i>,
    "<a href="#deletewithinstance" title="DeleteWithInstance">DeleteWithInstance</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#datadiskid" title="DataDiskId">DataDiskId</a>: <i>String</i>
<a href="#datadisksize" title="DataDiskSize">DataDiskSize</a>: <i>Double</i>
<a href="#datadisktype" title="DataDiskType">DataDiskType</a>: <i>String</i>
<a href="#deletewithinstance" title="DeleteWithInstance">DeleteWithInstance</a>: <i>Boolean</i>
</pre>

## Properties

#### DataDiskId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteWithInstance

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

