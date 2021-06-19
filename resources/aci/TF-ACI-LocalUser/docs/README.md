# TF::ACI::LocalUser

CloudFormation equivalent of aci_local_user

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::LocalUser",
    "Properties" : {
        "<a href="#accountstatus" title="AccountStatus">AccountStatus</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#certattribute" title="CertAttribute">CertAttribute</a>" : <i>String</i>,
        "<a href="#clearpwdhistory" title="ClearPwdHistory">ClearPwdHistory</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#expiration" title="Expiration">Expiration</a>" : <i>String</i>,
        "<a href="#expires" title="Expires">Expires</a>" : <i>String</i>,
        "<a href="#firstname" title="FirstName">FirstName</a>" : <i>String</i>,
        "<a href="#lastname" title="LastName">LastName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#otpenable" title="Otpenable">Otpenable</a>" : <i>String</i>,
        "<a href="#otpkey" title="Otpkey">Otpkey</a>" : <i>String</i>,
        "<a href="#phone" title="Phone">Phone</a>" : <i>String</i>,
        "<a href="#pwd" title="Pwd">Pwd</a>" : <i>String</i>,
        "<a href="#pwdlifetime" title="PwdLifeTime">PwdLifeTime</a>" : <i>String</i>,
        "<a href="#pwdupdaterequired" title="PwdUpdateRequired">PwdUpdateRequired</a>" : <i>String</i>,
        "<a href="#rbacstring" title="RbacString">RbacString</a>" : <i>String</i>,
        "<a href="#unixuserid" title="UnixUserId">UnixUserId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::LocalUser
Properties:
    <a href="#accountstatus" title="AccountStatus">AccountStatus</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#certattribute" title="CertAttribute">CertAttribute</a>: <i>String</i>
    <a href="#clearpwdhistory" title="ClearPwdHistory">ClearPwdHistory</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#expiration" title="Expiration">Expiration</a>: <i>String</i>
    <a href="#expires" title="Expires">Expires</a>: <i>String</i>
    <a href="#firstname" title="FirstName">FirstName</a>: <i>String</i>
    <a href="#lastname" title="LastName">LastName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#otpenable" title="Otpenable">Otpenable</a>: <i>String</i>
    <a href="#otpkey" title="Otpkey">Otpkey</a>: <i>String</i>
    <a href="#phone" title="Phone">Phone</a>: <i>String</i>
    <a href="#pwd" title="Pwd">Pwd</a>: <i>String</i>
    <a href="#pwdlifetime" title="PwdLifeTime">PwdLifeTime</a>: <i>String</i>
    <a href="#pwdupdaterequired" title="PwdUpdateRequired">PwdUpdateRequired</a>: <i>String</i>
    <a href="#rbacstring" title="RbacString">RbacString</a>: <i>String</i>
    <a href="#unixuserid" title="UnixUserId">UnixUserId</a>: <i>String</i>
</pre>

## Properties

#### AccountStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClearPwdHistory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expires

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Otpenable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Otpkey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pwd

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PwdLifeTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PwdUpdateRequired

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RbacString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnixUserId

_Required_: No

_Type_: String

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

