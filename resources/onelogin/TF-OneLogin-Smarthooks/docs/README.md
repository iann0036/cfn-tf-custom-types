# TF::OneLogin::Smarthooks

Manage SmartHook resources.

This resource allows you to create and configure SmartHooks.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OneLogin::Smarthooks",
    "Properties" : {
        "<a href="#contextversion" title="ContextVersion">ContextVersion</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#envvars" title="EnvVars">EnvVars</a>" : <i>[ String, ... ]</i>,
        "<a href="#function" title="Function">Function</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="optionsdefinition.md">OptionsDefinition</a>, ... ]</i>,
        "<a href="#packages" title="Packages">Packages</a>" : <i>[ <a href="packagesdefinition.md">PackagesDefinition</a>, ... ]</i>,
        "<a href="#retries" title="Retries">Retries</a>" : <i>Double</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditionsdefinition.md">ConditionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OneLogin::Smarthooks
Properties:
    <a href="#contextversion" title="ContextVersion">ContextVersion</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#envvars" title="EnvVars">EnvVars</a>: <i>
      - String</i>
    <a href="#function" title="Function">Function</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="optionsdefinition.md">OptionsDefinition</a></i>
    <a href="#packages" title="Packages">Packages</a>: <i>
      - <a href="packagesdefinition.md">PackagesDefinition</a></i>
    <a href="#retries" title="Retries">Retries</a>: <i>Double</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditionsdefinition.md">ConditionsDefinition</a></i>
</pre>

## Properties

#### ContextVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Indicates if function is available for execution or not. Default true.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvVars

An array of predefined environment variables to be supplied to the function at runtime.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Function

A base64 encoded blob, or Heredoc string containing the javascript function code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

A list of options for the hook
* `risk_enabled` - (Required) When true a risk score and risk reasons will be passed in the context. Only applies authentication time hooks. E.g. pre-authentication, user-migration. Default false.

_Required_: No

_Type_: List of <a href="optionsdefinition.md">OptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Packages

A list of public npm packages than will be installed as part of the function build process. These packages names must be on our allowlist. See Node Modules section of this doc. Packages can be any version and support the semantic versioning syntax used by NPM.

_Required_: Yes

_Type_: List of <a href="packagesdefinition.md">PackagesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retries

Number of retries if execution fails. Default 0, Max 4.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

The number of milliseconds to allow before timeout. Default 1000, Max 10000.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The name of the hook. Must be one of: `user-migration` `pre-authentication` `pre-user-create` `post-user-create` `pre-user-update` `post-user-update`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditionsdefinition.md">ConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Timestamp for smarthook's last update.

#### Id

Returns the <code>Id</code> value.

#### Status

The smarthook's status.

#### UpdatedAt

Timestamp for smarthook's last update.

