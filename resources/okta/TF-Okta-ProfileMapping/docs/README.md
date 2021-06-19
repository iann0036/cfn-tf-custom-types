# TF::Okta::ProfileMapping

Manages a profile mapping.

This resource allows you to manage a profile mapping by source id.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::ProfileMapping",
    "Properties" : {
        "<a href="#deletewhenabsent" title="DeleteWhenAbsent">DeleteWhenAbsent</a>" : <i>Boolean</i>,
        "<a href="#sourceid" title="SourceId">SourceId</a>" : <i>String</i>,
        "<a href="#targetid" title="TargetId">TargetId</a>" : <i>String</i>,
        "<a href="#mappings" title="Mappings">Mappings</a>" : <i>[ <a href="mappingsdefinition.md">MappingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::ProfileMapping
Properties:
    <a href="#deletewhenabsent" title="DeleteWhenAbsent">DeleteWhenAbsent</a>: <i>Boolean</i>
    <a href="#sourceid" title="SourceId">SourceId</a>: <i>String</i>
    <a href="#targetid" title="TargetId">TargetId</a>: <i>String</i>
    <a href="#mappings" title="Mappings">Mappings</a>: <i>
      - <a href="mappingsdefinition.md">MappingsDefinition</a></i>
</pre>

## Properties

#### DeleteWhenAbsent

Tells the provider whether to attempt to delete missing mappings under profile mapping.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceId

Source id of the profile mapping.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mappings

_Required_: No

_Type_: List of <a href="mappingsdefinition.md">MappingsDefinition</a>

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

Key of mapping.
- `expression` - (Required) Combination or single source properties that will be mapped to the target property.
- `push_status` - (Optional) Whether to update target properties on user create & update or just on create.

#### SourceName

Returns the <code>SourceName</code> value.

#### SourceType

Returns the <code>SourceType</code> value.

#### TargetName

Returns the <code>TargetName</code> value.

#### TargetType

Returns the <code>TargetType</code> value.

