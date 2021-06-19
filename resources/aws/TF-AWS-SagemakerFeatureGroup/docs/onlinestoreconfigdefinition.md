# TF::AWS::SagemakerFeatureGroup OnlineStoreConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enableonlinestore" title="EnableOnlineStore">EnableOnlineStore</a>" : <i>Boolean</i>,
    "<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>" : <i>[ <a href="securityconfigdefinition.md">SecurityConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enableonlinestore" title="EnableOnlineStore">EnableOnlineStore</a>: <i>Boolean</i>
<a href="#securityconfig" title="SecurityConfig">SecurityConfig</a>: <i>
      - <a href="securityconfigdefinition.md">SecurityConfigDefinition</a></i>
</pre>

## Properties

#### EnableOnlineStore

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfig

_Required_: No

_Type_: List of <a href="securityconfigdefinition.md">SecurityConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

