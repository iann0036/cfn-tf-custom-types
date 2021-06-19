# TF::AzureDevOps::ResourceAuthorization

Manages authorization of resources, e.g. for access in build pipelines.

Currently supported resources: service endpoint (aka service connection, endpoint).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::ResourceAuthorization",
    "Properties" : {
        "<a href="#authorized" title="Authorized">Authorized</a>" : <i>Boolean</i>,
        "<a href="#definitionid" title="DefinitionId">DefinitionId</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::ResourceAuthorization
Properties:
    <a href="#authorized" title="Authorized">Authorized</a>: <i>Boolean</i>
    <a href="#definitionid" title="DefinitionId">DefinitionId</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Authorized

Set to true to allow public access in the project. Type: boolean.
- `type` - (Optional) The type of the resource to authorize. Type: string. Valid values: `endpoint`, `queue`, `variablegroup`. Default value: `endpoint`.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinitionId

The ID of the build definition to authorize. Type: string.
- `authorized` - (Required) Set to true to allow public access in the project. Type: boolean.
- `type` - (Optional) The type of the resource to authorize. Type: string. Valid values: `endpoint`, `queue`, `variablegroup`. Default value: `endpoint`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name. Type: string.
- `resource_id` - (Required) The ID of the resource to authorize. Type: string.
- `definition_id` - (Optional) The ID of the build definition to authorize. Type: string.
- `authorized` - (Required) Set to true to allow public access in the project. Type: boolean.
- `type` - (Optional) The type of the resource to authorize. Type: string. Valid values: `endpoint`, `queue`, `variablegroup`. Default value: `endpoint`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

The ID of the resource to authorize. Type: string.
- `definition_id` - (Optional) The ID of the build definition to authorize. Type: string.
- `authorized` - (Required) Set to true to allow public access in the project. Type: boolean.
- `type` - (Optional) The type of the resource to authorize. Type: string. Valid values: `endpoint`, `queue`, `variablegroup`. Default value: `endpoint`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the resource to authorize. Type: string. Valid values: `endpoint`, `queue`, `variablegroup`. Default value: `endpoint`.

_Required_: No

_Type_: String

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

