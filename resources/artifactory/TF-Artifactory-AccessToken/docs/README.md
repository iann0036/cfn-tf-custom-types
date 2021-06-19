# TF::Artifactory::AccessToken

CloudFormation equivalent of artifactory_access_token

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Artifactory::AccessToken",
    "Properties" : {
        "<a href="#audience" title="Audience">Audience</a>" : <i>String</i>,
        "<a href="#enddate" title="EndDate">EndDate</a>" : <i>String</i>,
        "<a href="#enddaterelative" title="EndDateRelative">EndDateRelative</a>" : <i>String</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
        "<a href="#refreshable" title="Refreshable">Refreshable</a>" : <i>Boolean</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#admintoken" title="AdminToken">AdminToken</a>" : <i>[ <a href="admintokendefinition.md">AdminTokenDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Artifactory::AccessToken
Properties:
    <a href="#audience" title="Audience">Audience</a>: <i>String</i>
    <a href="#enddate" title="EndDate">EndDate</a>: <i>String</i>
    <a href="#enddaterelative" title="EndDateRelative">EndDateRelative</a>: <i>String</i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
    <a href="#refreshable" title="Refreshable">Refreshable</a>: <i>Boolean</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#admintoken" title="AdminToken">AdminToken</a>: <i>
      - <a href="admintokendefinition.md">AdminTokenDefinition</a></i>
</pre>

## Properties

#### Audience

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndDate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndDateRelative

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Refreshable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminToken

_Required_: No

_Type_: List of <a href="admintokendefinition.md">AdminTokenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccessToken

Returns the <code>AccessToken</code> value.

#### Id

Returns the <code>Id</code> value.

#### RefreshToken

Returns the <code>RefreshToken</code> value.

