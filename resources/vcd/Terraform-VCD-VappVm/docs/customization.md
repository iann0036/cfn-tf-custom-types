# Terraform::VCD::VappVm Customization

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#allowlocaladminpassword" title="AllowLocalAdminPassword">AllowLocalAdminPassword</a>" : <i>Boolean</i>,
    "<a href="#autogeneratepassword" title="AutoGeneratePassword">AutoGeneratePassword</a>" : <i>Boolean</i>,
    "<a href="#changesid" title="ChangeSid">ChangeSid</a>" : <i>Boolean</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#force" title="Force">Force</a>" : <i>Boolean</i>,
    "<a href="#initscript" title="Initscript">Initscript</a>" : <i>String</i>,
    "<a href="#joindomain" title="JoinDomain">JoinDomain</a>" : <i>Boolean</i>,
    "<a href="#joindomainaccountou" title="JoinDomainAccountOu">JoinDomainAccountOu</a>" : <i>String</i>,
    "<a href="#joindomainname" title="JoinDomainName">JoinDomainName</a>" : <i>String</i>,
    "<a href="#joindomainpassword" title="JoinDomainPassword">JoinDomainPassword</a>" : <i>String</i>,
    "<a href="#joindomainuser" title="JoinDomainUser">JoinDomainUser</a>" : <i>String</i>,
    "<a href="#joinorgdomain" title="JoinOrgDomain">JoinOrgDomain</a>" : <i>Boolean</i>,
    "<a href="#mustchangepasswordonfirstlogin" title="MustChangePasswordOnFirstLogin">MustChangePasswordOnFirstLogin</a>" : <i>Boolean</i>,
    "<a href="#numberofautologons" title="NumberOfAutoLogons">NumberOfAutoLogons</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#allowlocaladminpassword" title="AllowLocalAdminPassword">AllowLocalAdminPassword</a>: <i>Boolean</i>
<a href="#autogeneratepassword" title="AutoGeneratePassword">AutoGeneratePassword</a>: <i>Boolean</i>
<a href="#changesid" title="ChangeSid">ChangeSid</a>: <i>Boolean</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#force" title="Force">Force</a>: <i>Boolean</i>
<a href="#initscript" title="Initscript">Initscript</a>: <i>String</i>
<a href="#joindomain" title="JoinDomain">JoinDomain</a>: <i>Boolean</i>
<a href="#joindomainaccountou" title="JoinDomainAccountOu">JoinDomainAccountOu</a>: <i>String</i>
<a href="#joindomainname" title="JoinDomainName">JoinDomainName</a>: <i>String</i>
<a href="#joindomainpassword" title="JoinDomainPassword">JoinDomainPassword</a>: <i>String</i>
<a href="#joindomainuser" title="JoinDomainUser">JoinDomainUser</a>: <i>String</i>
<a href="#joinorgdomain" title="JoinOrgDomain">JoinOrgDomain</a>: <i>Boolean</i>
<a href="#mustchangepasswordonfirstlogin" title="MustChangePasswordOnFirstLogin">MustChangePasswordOnFirstLogin</a>: <i>Boolean</i>
<a href="#numberofautologons" title="NumberOfAutoLogons">NumberOfAutoLogons</a>: <i>Double</i>
</pre>

## Properties

#### AdminPassword

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowLocalAdminPassword

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoGeneratePassword

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeSid

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Force

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initscript

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JoinDomain

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JoinDomainAccountOu

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JoinDomainName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JoinDomainPassword

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JoinDomainUser

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JoinOrgDomain

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustChangePasswordOnFirstLogin

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfAutoLogons

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

