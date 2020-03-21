# Terraform::VCD::VappVm OverrideTemplateDisk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#busnumber" title="BusNumber">BusNumber</a>" : <i>Double</i>,
    "<a href="#bustype" title="BusType">BusType</a>" : <i>String</i>,
    "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
    "<a href="#sizeinmb" title="SizeInMb">SizeInMb</a>" : <i>Double</i>,
    "<a href="#storageprofile" title="StorageProfile">StorageProfile</a>" : <i>String</i>,
    "<a href="#unitnumber" title="UnitNumber">UnitNumber</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#busnumber" title="BusNumber">BusNumber</a>: <i>Double</i>
<a href="#bustype" title="BusType">BusType</a>: <i>String</i>
<a href="#iops" title="Iops">Iops</a>: <i>Double</i>
<a href="#sizeinmb" title="SizeInMb">SizeInMb</a>: <i>Double</i>
<a href="#storageprofile" title="StorageProfile">StorageProfile</a>: <i>String</i>
<a href="#unitnumber" title="UnitNumber">UnitNumber</a>: <i>Double</i>
</pre>

## Properties

#### BusNumber

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BusType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iops

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeInMb

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitNumber

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

