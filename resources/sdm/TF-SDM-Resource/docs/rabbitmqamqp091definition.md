# TF::SDM::Resource RabbitmqAmqp091Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#egressfilter" title="EgressFilter">EgressFilter</a>" : <i>String</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>" : <i>String</i>,
    "<a href="#secretstorepasswordkey" title="SecretStorePasswordKey">SecretStorePasswordKey</a>" : <i>String</i>,
    "<a href="#secretstorepasswordpath" title="SecretStorePasswordPath">SecretStorePasswordPath</a>" : <i>String</i>,
    "<a href="#secretstoreusernamekey" title="SecretStoreUsernameKey">SecretStoreUsernameKey</a>" : <i>String</i>,
    "<a href="#secretstoreusernamepath" title="SecretStoreUsernamePath">SecretStoreUsernamePath</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
    "<a href="#tlsrequired" title="TlsRequired">TlsRequired</a>" : <i>Boolean</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#egressfilter" title="EgressFilter">EgressFilter</a>: <i>String</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>: <i>String</i>
<a href="#secretstorepasswordkey" title="SecretStorePasswordKey">SecretStorePasswordKey</a>: <i>String</i>
<a href="#secretstorepasswordpath" title="SecretStorePasswordPath">SecretStorePasswordPath</a>: <i>String</i>
<a href="#secretstoreusernamekey" title="SecretStoreUsernameKey">SecretStoreUsernameKey</a>: <i>String</i>
<a href="#secretstoreusernamepath" title="SecretStoreUsernamePath">SecretStoreUsernamePath</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
<a href="#tlsrequired" title="TlsRequired">TlsRequired</a>: <i>Boolean</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### EgressFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStorePasswordKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStorePasswordPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreUsernameKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreUsernamePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsRequired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

