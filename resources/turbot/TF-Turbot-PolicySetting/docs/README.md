# TF::Turbot::PolicySetting

The `Turbot Policy Setting` resource adds support for setting policies for resources. It is used to create, update and delete policy settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::PolicySetting",
    "Properties" : {
        "<a href="#note" title="Note">Note</a>" : <i>String</i>,
        "<a href="#pgpkey" title="PgpKey">PgpKey</a>" : <i>String</i>,
        "<a href="#precedence" title="Precedence">Precedence</a>" : <i>String</i>,
        "<a href="#resource" title="Resource">Resource</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templateinput" title="TemplateInput">TemplateInput</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#validfromtimestamp" title="ValidFromTimestamp">ValidFromTimestamp</a>" : <i>String</i>,
        "<a href="#validtotimestamp" title="ValidToTimestamp">ValidToTimestamp</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::PolicySetting
Properties:
    <a href="#note" title="Note">Note</a>: <i>String</i>
    <a href="#pgpkey" title="PgpKey">PgpKey</a>: <i>String</i>
    <a href="#precedence" title="Precedence">Precedence</a>: <i>String</i>
    <a href="#resource" title="Resource">Resource</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templateinput" title="TemplateInput">TemplateInput</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#validfromtimestamp" title="ValidFromTimestamp">ValidFromTimestamp</a>: <i>String</i>
    <a href="#validtotimestamp" title="ValidToTimestamp">ValidToTimestamp</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### Note

Additional notes, if desired.
- `precedence` - (Optional) Determines whether the policy setting should be `required` or `recommended`. Defaults to `required`.
- `template` - (Optional) Nunjucks template that is used to render the policy.
- `template_input` - (Optional) A GraphQL query as a `string` or array of GraphQL queries in `YAML` format. The GraphQL output is used as the render context when rendering the `template`
- `valid_from_timestamp` - (Optional) The start of a specific time period for which the policy setting is valid.
- `valid_to_timestamp` - (Optional) The expiration date of a policy value.
- `value` - (Optional) Value of the policy. This could either be the value of the setting or a `yaml` string representing the setting.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PgpKey

A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Precedence

Determines whether the policy setting should be `required` or `recommended`. Defaults to `required`.
- `template` - (Optional) Nunjucks template that is used to render the policy.
- `template_input` - (Optional) A GraphQL query as a `string` or array of GraphQL queries in `YAML` format. The GraphQL output is used as the render context when rendering the `template`
- `valid_from_timestamp` - (Optional) The start of a specific time period for which the policy setting is valid.
- `valid_to_timestamp` - (Optional) The expiration date of a policy value.
- `value` - (Optional) Value of the policy. This could either be the value of the setting or a `yaml` string representing the setting.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resource

The `aka` of the resource.
- `note` - (Optional) Additional notes, if desired.
- `precedence` - (Optional) Determines whether the policy setting should be `required` or `recommended`. Defaults to `required`.
- `template` - (Optional) Nunjucks template that is used to render the policy.
- `template_input` - (Optional) A GraphQL query as a `string` or array of GraphQL queries in `YAML` format. The GraphQL output is used as the render context when rendering the `template`
- `valid_from_timestamp` - (Optional) The start of a specific time period for which the policy setting is valid.
- `valid_to_timestamp` - (Optional) The expiration date of a policy value.
- `value` - (Optional) Value of the policy. This could either be the value of the setting or a `yaml` string representing the setting.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

Nunjucks template that is used to render the policy.
- `template_input` - (Optional) A GraphQL query as a `string` or array of GraphQL queries in `YAML` format. The GraphQL output is used as the render context when rendering the `template`
- `valid_from_timestamp` - (Optional) The start of a specific time period for which the policy setting is valid.
- `valid_to_timestamp` - (Optional) The expiration date of a policy value.
- `value` - (Optional) Value of the policy. This could either be the value of the setting or a `yaml` string representing the setting.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateInput

A GraphQL query as a `string` or array of GraphQL queries in `YAML` format. The GraphQL output is used as the render context when rendering the `template`
- `valid_from_timestamp` - (Optional) The start of a specific time period for which the policy setting is valid.
- `valid_to_timestamp` - (Optional) The expiration date of a policy value.
- `value` - (Optional) Value of the policy. This could either be the value of the setting or a `yaml` string representing the setting.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The `aka` of the policy type to be created. This is represented by `uri` which can be found out from the overview section of the desired policy.
- `resource` - (Required) The `aka` of the resource.
- `note` - (Optional) Additional notes, if desired.
- `precedence` - (Optional) Determines whether the policy setting should be `required` or `recommended`. Defaults to `required`.
- `template` - (Optional) Nunjucks template that is used to render the policy.
- `template_input` - (Optional) A GraphQL query as a `string` or array of GraphQL queries in `YAML` format. The GraphQL output is used as the render context when rendering the `template`
- `valid_from_timestamp` - (Optional) The start of a specific time period for which the policy setting is valid.
- `valid_to_timestamp` - (Optional) The expiration date of a policy value.
- `value` - (Optional) Value of the policy. This could either be the value of the setting or a `yaml` string representing the setting.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidFromTimestamp

The start of a specific time period for which the policy setting is valid.
- `valid_to_timestamp` - (Optional) The expiration date of a policy value.
- `value` - (Optional) Value of the policy. This could either be the value of the setting or a `yaml` string representing the setting.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidToTimestamp

The expiration date of a policy value.
- `value` - (Optional) Value of the policy. This could either be the value of the setting or a `yaml` string representing the setting.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

Value of the policy. This could either be the value of the setting or a `yaml` string representing the setting.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

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

#### ResourceAkas

Returns the <code>ResourceAkas</code> value.

#### ValueKeyFingerprint

Returns the <code>ValueKeyFingerprint</code> value.

#### ValueSource

Returns the <code>ValueSource</code> value.

#### ValueSourceKeyFingerprint

Returns the <code>ValueSourceKeyFingerprint</code> value.

#### ValueSourceUsed

Returns the <code>ValueSourceUsed</code> value.

