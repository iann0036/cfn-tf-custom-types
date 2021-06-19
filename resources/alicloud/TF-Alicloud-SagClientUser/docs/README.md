# TF::Alicloud::SagClientUser

Provides a Sag ClientUser resource. This topic describes how to manage accounts as an administrator. After you configure the network, you can create multiple accounts and distribute them to end users so that clients can access Alibaba Cloud.

For information about Sag ClientUser and how to use it, see [What is Sag ClientUser](https://www.alibabacloud.com/help/doc-detail/108326.htm).

-> **NOTE:** Available in 1.65.0+

-> **NOTE:** Only the following regions support. [`cn-shanghai`, `cn-shanghai-finance-1`, `cn-hongkong`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-5`, `ap-northeast-1`, `eu-central-1`]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::SagClientUser",
    "Properties" : {
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#clientip" title="ClientIp">ClientIp</a>" : <i>String</i>,
        "<a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>" : <i>String</i>,
        "<a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>" : <i>[ <a href="kmsencryptioncontextdefinition.md">KmsEncryptionContextDefinition</a>, ... ]</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#sagid" title="SagId">SagId</a>" : <i>String</i>,
        "<a href="#usermail" title="UserMail">UserMail</a>" : <i>String</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::SagClientUser
Properties:
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#clientip" title="ClientIp">ClientIp</a>: <i>String</i>
    <a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>: <i>String</i>
    <a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>: <i>
      - <a href="kmsencryptioncontextdefinition.md">KmsEncryptionContextDefinition</a></i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#sagid" title="SagId">SagId</a>: <i>String</i>
    <a href="#usermail" title="UserMail">UserMail</a>: <i>String</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
</pre>

## Properties

#### Bandwidth

The SAG APP bandwidth that the user can use. Unit: Kbit/s. Maximum value: 2000 Kbit/s.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIp

The IP address of the SAG APP. If you specify this parameter, the current account always uses the specified IP address.Note The IP address must be in the private CIDR block of the SAG client.If you do not specify this parameter, the system automatically allocates an IP address from the private CIDR block of the SAG client. In this case, each re-connection uses a different IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptedPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptionContext

_Required_: No

_Type_: List of <a href="kmsencryptioncontextdefinition.md">KmsEncryptionContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password used to log on to the SAG APP.Both the user name and the password must be specified. If you specify the user name, the password must be specified, too.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SagId

The ID of the SAG instance created for the SAG APP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserMail

The email address of the user. The administrator uses this address to send the account information for logging on to the APP to the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

The user name. User names in the same SAG APP must be unique.Both the user name and the password must be specified. If you specify the user name, the password must be specified, too.

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

