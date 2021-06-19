# TF::Alicloud::EssScalinggroupVserverGroups VserverGroupsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>" : <i>String</i>,
    "<a href="#vserverattributes" title="VserverAttributes">VserverAttributes</a>" : <i>[ <a href="vserverattributesdefinition.md">VserverAttributesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>: <i>String</i>
<a href="#vserverattributes" title="VserverAttributes">VserverAttributes</a>: <i>
      - <a href="vserverattributesdefinition.md">VserverAttributesDefinition</a></i>
</pre>

## Properties

#### LoadbalancerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VserverAttributes

_Required_: No

_Type_: List of <a href="vserverattributesdefinition.md">VserverAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

