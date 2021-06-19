# TF::Alicloud::FcCustomDomain RouteConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
    "<a href="#methods" title="Methods">Methods</a>" : <i>[ String, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#qualifier" title="Qualifier">Qualifier</a>" : <i>String</i>,
    "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
<a href="#methods" title="Methods">Methods</a>: <i>
      - String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#qualifier" title="Qualifier">Qualifier</a>: <i>String</i>
<a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
</pre>

## Properties

#### FunctionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Methods

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Qualifier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

