# Terraform::VSphere::VirtualMachine WindowsOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#autologon" title="AutoLogon">AutoLogon</a>" : <i>Boolean</i>,
    "<a href="#autologoncount" title="AutoLogonCount">AutoLogonCount</a>" : <i>Double</i>,
    "<a href="#computername" title="ComputerName">ComputerName</a>" : <i>String</i>,
    "<a href="#domainadminpassword" title="DomainAdminPassword">DomainAdminPassword</a>" : <i>String</i>,
    "<a href="#domainadminuser" title="DomainAdminUser">DomainAdminUser</a>" : <i>String</i>,
    "<a href="#fullname" title="FullName">FullName</a>" : <i>String</i>,
    "<a href="#joindomain" title="JoinDomain">JoinDomain</a>" : <i>String</i>,
    "<a href="#organizationname" title="OrganizationName">OrganizationName</a>" : <i>String</i>,
    "<a href="#productkey" title="ProductKey">ProductKey</a>" : <i>String</i>,
    "<a href="#runoncecommandlist" title="RunOnceCommandList">RunOnceCommandList</a>" : <i>[ String, ... ]</i>,
    "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>Double</i>,
    "<a href="#workgroup" title="Workgroup">Workgroup</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#autologon" title="AutoLogon">AutoLogon</a>: <i>Boolean</i>
<a href="#autologoncount" title="AutoLogonCount">AutoLogonCount</a>: <i>Double</i>
<a href="#computername" title="ComputerName">ComputerName</a>: <i>String</i>
<a href="#domainadminpassword" title="DomainAdminPassword">DomainAdminPassword</a>: <i>String</i>
<a href="#domainadminuser" title="DomainAdminUser">DomainAdminUser</a>: <i>String</i>
<a href="#fullname" title="FullName">FullName</a>: <i>String</i>
<a href="#joindomain" title="JoinDomain">JoinDomain</a>: <i>String</i>
<a href="#organizationname" title="OrganizationName">OrganizationName</a>: <i>String</i>
<a href="#productkey" title="ProductKey">ProductKey</a>: <i>String</i>
<a href="#runoncecommandlist" title="RunOnceCommandList">RunOnceCommandList</a>: <i>
      - String</i>
<a href="#timezone" title="TimeZone">TimeZone</a>: <i>Double</i>
<a href="#workgroup" title="Workgroup">Workgroup</a>: <i>String</i>
</pre>

## Properties

#### AdminPassword

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoLogon

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoLogonCount

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputerName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainAdminPassword

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainAdminUser

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JoinDomain

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductKey

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunOnceCommandList

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Workgroup

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

