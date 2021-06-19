# TF::Fastly::ServiceV1 WafDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#prefetchcondition" title="PrefetchCondition">PrefetchCondition</a>" : <i>String</i>,
    "<a href="#responseobject" title="ResponseObject">ResponseObject</a>" : <i>[ <a href="responseobjectdefinition.md">ResponseObjectDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#prefetchcondition" title="PrefetchCondition">PrefetchCondition</a>: <i>String</i>
<a href="#responseobject" title="ResponseObject">ResponseObject</a>: <i>
      - <a href="responseobjectdefinition.md">ResponseObjectDefinition</a></i>
</pre>

## Properties

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefetchCondition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseObject

_Required_: Yes

_Type_: List of <a href="responseobjectdefinition.md">ResponseObjectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

