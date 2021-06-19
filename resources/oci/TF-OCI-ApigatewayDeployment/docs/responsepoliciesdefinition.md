# TF::OCI::ApigatewayDeployment ResponsePoliciesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headertransformations" title="HeaderTransformations">HeaderTransformations</a>" : <i>[ <a href="headertransformationsdefinition.md">HeaderTransformationsDefinition</a>, ... ]</i>,
    "<a href="#responsecachestore" title="ResponseCacheStore">ResponseCacheStore</a>" : <i>[ <a href="responsecachestoredefinition.md">ResponseCacheStoreDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#headertransformations" title="HeaderTransformations">HeaderTransformations</a>: <i>
      - <a href="headertransformationsdefinition.md">HeaderTransformationsDefinition</a></i>
<a href="#responsecachestore" title="ResponseCacheStore">ResponseCacheStore</a>: <i>
      - <a href="responsecachestoredefinition.md">ResponseCacheStoreDefinition</a></i>
</pre>

## Properties

#### HeaderTransformations

_Required_: No

_Type_: List of <a href="headertransformationsdefinition.md">HeaderTransformationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCacheStore

_Required_: No

_Type_: List of <a href="responsecachestoredefinition.md">ResponseCacheStoreDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

