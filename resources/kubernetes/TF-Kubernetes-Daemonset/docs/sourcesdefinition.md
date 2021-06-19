# TF::Kubernetes::Daemonset SourcesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configmap" title="ConfigMap">ConfigMap</a>" : <i>[ <a href="configmapdefinition.md">ConfigMapDefinition</a>, ... ]</i>,
    "<a href="#downwardapi" title="DownwardApi">DownwardApi</a>" : <i>[ <a href="downwardapidefinition.md">DownwardApiDefinition</a>, ... ]</i>,
    "<a href="#secret" title="Secret">Secret</a>" : <i>[ <a href="secretdefinition.md">SecretDefinition</a>, ... ]</i>,
    "<a href="#serviceaccounttoken" title="ServiceAccountToken">ServiceAccountToken</a>" : <i>[ <a href="serviceaccounttokendefinition.md">ServiceAccountTokenDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configmap" title="ConfigMap">ConfigMap</a>: <i>
      - <a href="configmapdefinition.md">ConfigMapDefinition</a></i>
<a href="#downwardapi" title="DownwardApi">DownwardApi</a>: <i>
      - <a href="downwardapidefinition.md">DownwardApiDefinition</a></i>
<a href="#secret" title="Secret">Secret</a>: <i>
      - <a href="secretdefinition.md">SecretDefinition</a></i>
<a href="#serviceaccounttoken" title="ServiceAccountToken">ServiceAccountToken</a>: <i>
      - <a href="serviceaccounttokendefinition.md">ServiceAccountTokenDefinition</a></i>
</pre>

## Properties

#### ConfigMap

_Required_: No

_Type_: List of <a href="configmapdefinition.md">ConfigMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownwardApi

_Required_: No

_Type_: List of <a href="downwardapidefinition.md">DownwardApiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: No

_Type_: List of <a href="secretdefinition.md">SecretDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountToken

_Required_: No

_Type_: List of <a href="serviceaccounttokendefinition.md">ServiceAccountTokenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

