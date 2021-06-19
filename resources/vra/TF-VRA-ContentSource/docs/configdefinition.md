# TF::VRA::ContentSource ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#branch" title="Branch">Branch</a>" : <i>String</i>,
    "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
    "<a href="#integrationid" title="IntegrationId">IntegrationId</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
    "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#branch" title="Branch">Branch</a>: <i>String</i>
<a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
<a href="#integrationid" title="IntegrationId">IntegrationId</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
<a href="#repository" title="Repository">Repository</a>: <i>String</i>
</pre>

## Properties

#### Branch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

