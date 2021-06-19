# TF::SDM::Resource KubernetesServiceAccountDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#egressfilter" title="EgressFilter">EgressFilter</a>" : <i>String</i>,
    "<a href="#healthchecknamespace" title="HealthcheckNamespace">HealthcheckNamespace</a>" : <i>String</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>" : <i>String</i>,
    "<a href="#secretstoretokenkey" title="SecretStoreTokenKey">SecretStoreTokenKey</a>" : <i>String</i>,
    "<a href="#secretstoretokenpath" title="SecretStoreTokenPath">SecretStoreTokenPath</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
    "<a href="#token" title="Token">Token</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#egressfilter" title="EgressFilter">EgressFilter</a>: <i>String</i>
<a href="#healthchecknamespace" title="HealthcheckNamespace">HealthcheckNamespace</a>: <i>String</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>: <i>String</i>
<a href="#secretstoretokenkey" title="SecretStoreTokenKey">SecretStoreTokenKey</a>: <i>String</i>
<a href="#secretstoretokenpath" title="SecretStoreTokenPath">SecretStoreTokenPath</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
<a href="#token" title="Token">Token</a>: <i>String</i>
</pre>

## Properties

#### EgressFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckNamespace

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

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreTokenKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreTokenPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

