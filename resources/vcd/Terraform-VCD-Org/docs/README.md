# Terraform::VCD::Org

Provides a vCloud Director Org resource. This can be used to create, update, and delete an organization.
Requires system administrator privileges.

Supported in provider *v2.0+*

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

- True if this organization is allowed to share catalogs. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayAfterPowerOnSeconds

- Specifies this organization's default for virtual machine boot delay after power on. Default is `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteForce

- pass `delete_force=true` and `delete_recursive=true` to remove an organization or VDC and any objects it contains, regardless of their state.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteRecursive

- pass `delete_recursive`=true as query parameter to remove an organization or VDC and any objects it contains that are in a state that normally allows removal.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployedVmQuota

- Maximum number of virtual machines that can be deployed simultaneously by a member of this organization. Default is unlimited (0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

- Org description. Default is empty.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullName

Org full name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

- True if this organization is enabled (allows login and all other operations). Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Org name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoredVmQuota

- Maximum number of virtual machines in vApps or vApp templates that can be stored in an undeployed state by a member of this organization. Default is unlimited (0).

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

