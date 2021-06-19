# TF::AWS::CloudfrontOriginRequestPolicy QueryStringsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#querystringbehavior" title="QueryStringBehavior">QueryStringBehavior</a>" : <i>String</i>,
    "<a href="#querystrings" title="QueryStrings">QueryStrings</a>" : <i>[ <a href="querystringsdefinition.md">QueryStringsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#querystringbehavior" title="QueryStringBehavior">QueryStringBehavior</a>: <i>String</i>
<a href="#querystrings" title="QueryStrings">QueryStrings</a>: <i>
      - <a href="querystringsdefinition.md">QueryStringsDefinition</a></i>
</pre>

## Properties

#### QueryStringBehavior

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryStrings

_Required_: No

_Type_: List of <a href="querystringsdefinition.md">QueryStringsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

