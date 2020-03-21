# Terraform::VCD::Org

CloudFormation equivalent of vcd_org

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::Org",
    "Properties" : {
        "<a href="#canpublishcatalogs" title="CanPublishCatalogs">CanPublishCatalogs</a>" : <i>Boolean</i>,
        "<a href="#delayafterpoweronseconds" title="DelayAfterPowerOnSeconds">DelayAfterPowerOnSeconds</a>" : <i>Double</i>,
        "<a href="#deleteforce" title="DeleteForce">DeleteForce</a>" : <i>Boolean</i>,
        "<a href="#deleterecursive" title="DeleteRecursive">DeleteRecursive</a>" : <i>Boolean</i>,
        "<a href="#deployedvmquota" title="DeployedVmQuota">DeployedVmQuota</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#fullname" title="FullName">FullName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#storedvmquota" title="StoredVmQuota">StoredVmQuota</a>" : <i>Double</i>,
        "<a href="#vapplease" title="VappLease">VappLease</a>" : <i>[ <a href="vapplease.md">VappLease</a>, ... ]</i>,
        "<a href="#vapptemplatelease" title="VappTemplateLease">VappTemplateLease</a>" : <i>[ <a href="vapptemplatelease.md">VappTemplateLease</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::Org
Properties:
    <a href="#canpublishcatalogs" title="CanPublishCatalogs">CanPublishCatalogs</a>: <i>Boolean</i>
    <a href="#delayafterpoweronseconds" title="DelayAfterPowerOnSeconds">DelayAfterPowerOnSeconds</a>: <i>Double</i>
    <a href="#deleteforce" title="DeleteForce">DeleteForce</a>: <i>Boolean</i>
    <a href="#deleterecursive" title="DeleteRecursive">DeleteRecursive</a>: <i>Boolean</i>
    <a href="#deployedvmquota" title="DeployedVmQuota">DeployedVmQuota</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#fullname" title="FullName">FullName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#storedvmquota" title="StoredVmQuota">StoredVmQuota</a>: <i>Double</i>
    <a href="#vapplease" title="VappLease">VappLease</a>: <i>
      - <a href="vapplease.md">VappLease</a></i>
    <a href="#vapptemplatelease" title="VappTemplateLease">VappTemplateLease</a>: <i>
      - <a href="vapptemplatelease.md">VappTemplateLease</a></i>
</pre>

## Properties

#### CanPublishCatalogs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayAfterPowerOnSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteForce

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteRecursive

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployedVmQuota

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoredVmQuota

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappLease

_Required_: No

_Type_: List of <a href="vapplease.md">VappLease</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappTemplateLease

_Required_: No

_Type_: List of <a href="vapptemplatelease.md">VappTemplateLease</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
