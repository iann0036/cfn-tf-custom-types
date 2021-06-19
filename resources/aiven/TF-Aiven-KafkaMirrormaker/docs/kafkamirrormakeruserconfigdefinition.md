# TF::Aiven::KafkaMirrormaker KafkaMirrormakerUserConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipfilter" title="IpFilter">IpFilter</a>" : <i>[ String, ... ]</i>,
    "<a href="#kafkamirrormaker" title="KafkaMirrormaker">KafkaMirrormaker</a>" : <i>[ <a href="kafkamirrormakerdefinition.md">KafkaMirrormakerDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipfilter" title="IpFilter">IpFilter</a>: <i>
      - String</i>
<a href="#kafkamirrormaker" title="KafkaMirrormaker">KafkaMirrormaker</a>: <i>
      - <a href="kafkamirrormakerdefinition.md">KafkaMirrormakerDefinition</a></i>
</pre>

## Properties

#### IpFilter

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaMirrormaker

_Required_: No

_Type_: List of <a href="kafkamirrormakerdefinition.md">KafkaMirrormakerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

