# TF::Kubernetes::ValidatingWebhookConfiguration ClientConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cabundle" title="CaBundle">CaBundle</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#service" title="Service">Service</a>" : <i>[ <a href="servicedefinition.md">ServiceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cabundle" title="CaBundle">CaBundle</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#service" title="Service">Service</a>: <i>
      - <a href="servicedefinition.md">ServiceDefinition</a></i>
</pre>

## Properties

#### CaBundle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="servicedefinition.md">ServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

