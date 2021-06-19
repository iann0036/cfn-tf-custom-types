# TF::SignalFx::DataLink

Manage SignalFx [Data Links](https://docs.signalfx.com/en/latest/managing/data-links.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::DataLink",
    "Properties" : {
        "<a href="#contextdashboardid" title="ContextDashboardId">ContextDashboardId</a>" : <i>String</i>,
        "<a href="#propertyname" title="PropertyName">PropertyName</a>" : <i>String</i>,
        "<a href="#propertyvalue" title="PropertyValue">PropertyValue</a>" : <i>String</i>,
        "<a href="#targetexternalurl" title="TargetExternalUrl">TargetExternalUrl</a>" : <i>[ <a href="targetexternalurldefinition.md">TargetExternalUrlDefinition</a>, ... ]</i>,
        "<a href="#targetsignalfxdashboard" title="TargetSignalfxDashboard">TargetSignalfxDashboard</a>" : <i>[ <a href="targetsignalfxdashboarddefinition.md">TargetSignalfxDashboardDefinition</a>, ... ]</i>,
        "<a href="#targetsplunk" title="TargetSplunk">TargetSplunk</a>" : <i>[ <a href="targetsplunkdefinition.md">TargetSplunkDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::DataLink
Properties:
    <a href="#contextdashboardid" title="ContextDashboardId">ContextDashboardId</a>: <i>String</i>
    <a href="#propertyname" title="PropertyName">PropertyName</a>: <i>String</i>
    <a href="#propertyvalue" title="PropertyValue">PropertyValue</a>: <i>String</i>
    <a href="#targetexternalurl" title="TargetExternalUrl">TargetExternalUrl</a>: <i>
      - <a href="targetexternalurldefinition.md">TargetExternalUrlDefinition</a></i>
    <a href="#targetsignalfxdashboard" title="TargetSignalfxDashboard">TargetSignalfxDashboard</a>: <i>
      - <a href="targetsignalfxdashboarddefinition.md">TargetSignalfxDashboardDefinition</a></i>
    <a href="#targetsplunk" title="TargetSplunk">TargetSplunk</a>: <i>
      - <a href="targetsplunkdefinition.md">TargetSplunkDefinition</a></i>
</pre>

## Properties

#### ContextDashboardId

If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertyName

Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertyValue

Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetExternalUrl

_Required_: No

_Type_: List of <a href="targetexternalurldefinition.md">TargetExternalUrlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSignalfxDashboard

_Required_: No

_Type_: List of <a href="targetsignalfxdashboarddefinition.md">TargetSignalfxDashboardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSplunk

_Required_: No

_Type_: List of <a href="targetsplunkdefinition.md">TargetSplunkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

