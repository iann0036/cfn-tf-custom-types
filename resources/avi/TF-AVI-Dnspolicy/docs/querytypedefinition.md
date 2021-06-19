# TF::AVI::Dnspolicy QueryTypeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>" : <i>String</i>,
    "<a href="#querytype" title="QueryType">QueryType</a>" : <i>[ <a href="querytypedefinition.md">QueryTypeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>: <i>String</i>
<a href="#querytype" title="QueryType">QueryType</a>: <i>
      - <a href="querytypedefinition.md">QueryTypeDefinition</a></i>
</pre>

## Properties

#### MatchCriteria

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryType

_Required_: No

_Type_: List of <a href="querytypedefinition.md">QueryTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

