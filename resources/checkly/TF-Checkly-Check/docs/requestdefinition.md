# TF::Checkly::Check RequestDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#body" title="Body">Body</a>" : <i>String</i>,
    "<a href="#bodytype" title="BodyType">BodyType</a>" : <i>String</i>,
    "<a href="#followredirects" title="FollowRedirects">FollowRedirects</a>" : <i>Boolean</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#queryparameters" title="QueryParameters">QueryParameters</a>" : <i>[ <a href="queryparametersdefinition.md">QueryParametersDefinition</a>, ... ]</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#assertion" title="Assertion">Assertion</a>" : <i>[ <a href="assertiondefinition.md">AssertionDefinition</a>, ... ]</i>,
    "<a href="#basicauth" title="BasicAuth">BasicAuth</a>" : <i>[ <a href="basicauthdefinition.md">BasicAuthDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#body" title="Body">Body</a>: <i>String</i>
<a href="#bodytype" title="BodyType">BodyType</a>: <i>String</i>
<a href="#followredirects" title="FollowRedirects">FollowRedirects</a>: <i>Boolean</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#queryparameters" title="QueryParameters">QueryParameters</a>: <i>
      - <a href="queryparametersdefinition.md">QueryParametersDefinition</a></i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#assertion" title="Assertion">Assertion</a>: <i>
      - <a href="assertiondefinition.md">AssertionDefinition</a></i>
<a href="#basicauth" title="BasicAuth">BasicAuth</a>: <i>
      - <a href="basicauthdefinition.md">BasicAuthDefinition</a></i>
</pre>

## Properties

#### Body

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BodyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowRedirects

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameters

_Required_: No

_Type_: List of <a href="queryparametersdefinition.md">QueryParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Assertion

_Required_: No

_Type_: List of <a href="assertiondefinition.md">AssertionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuth

_Required_: No

_Type_: List of <a href="basicauthdefinition.md">BasicAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

