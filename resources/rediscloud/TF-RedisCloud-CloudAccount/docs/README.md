# TF::RedisCloud::CloudAccount

Creates a Cloud Account resource representing the access credentials to a cloud provider account, (`AWS`).
Redis Enterprise Cloud uses these credentials to provision databases within your infrastructure.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::RedisCloud::CloudAccount",
    "Properties" : {
        "<a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>" : <i>String</i>,
        "<a href="#accesssecretkey" title="AccessSecretKey">AccessSecretKey</a>" : <i>String</i>,
        "<a href="#consolepassword" title="ConsolePassword">ConsolePassword</a>" : <i>String</i>,
        "<a href="#consoleusername" title="ConsoleUsername">ConsoleUsername</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#providertype" title="ProviderType">ProviderType</a>" : <i>String</i>,
        "<a href="#signinloginurl" title="SignInLoginUrl">SignInLoginUrl</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::RedisCloud::CloudAccount
Properties:
    <a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>: <i>String</i>
    <a href="#accesssecretkey" title="AccessSecretKey">AccessSecretKey</a>: <i>String</i>
    <a href="#consolepassword" title="ConsolePassword">ConsolePassword</a>: <i>String</i>
    <a href="#consoleusername" title="ConsoleUsername">ConsoleUsername</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#providertype" title="ProviderType">ProviderType</a>: <i>String</i>
    <a href="#signinloginurl" title="SignInLoginUrl">SignInLoginUrl</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessKeyId

Cloud provider access key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessSecretKey

Cloud provider secret key.
Note that drift cannot currently be detected for this.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsolePassword

Cloud provider management console password.
Note that drift cannot currently be detected for this.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsoleUsername

Cloud provider management console username.
Note that drift cannot currently be detected for this.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Display name of the account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderType

Cloud provider type - either `AWS` or `GCP`.
Note that drift cannot currently be detected for this.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignInLoginUrl

Cloud provider management console login URL.
Note that drift cannot currently be detected for this.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Status

Returns the <code>Status</code> value.

