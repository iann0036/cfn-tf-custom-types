# TF::AVI::Httppolicyset IpReputationTypeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchoperation" title="MatchOperation">MatchOperation</a>" : <i>String</i>,
    "<a href="#reputationtypes" title="ReputationTypes">ReputationTypes</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchoperation" title="MatchOperation">MatchOperation</a>: <i>String</i>
<a href="#reputationtypes" title="ReputationTypes">ReputationTypes</a>: <i>
      - String</i>
</pre>

## Properties

#### MatchOperation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReputationTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

