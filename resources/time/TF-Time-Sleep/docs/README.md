# TF::Time::Sleep

Manages a resource that delays creation and/or destruction, typically for further resources. This prevents cross-platform compatibility and destroy-time issues with using the [`local-exec` provisioner](https://www.terraform.io/docs/provisioners/local-exec.html).

-> In many cases, this resource should be considered a workaround for issues that should be reported and handled in downstream Terraform Provider logic. Downstream resources can usually introduce or adjust retries in their code to handle time delay issues for all Terraform configurations or upstream resources can be improved to better wait for a resource to be fully ready and available.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Time::Sleep",
    "Properties" : {
        "<a href="#createduration" title="CreateDuration">CreateDuration</a>" : <i>String</i>,
        "<a href="#destroyduration" title="DestroyDuration">DestroyDuration</a>" : <i>String</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ <a href="triggersdefinition.md">TriggersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Time::Sleep
Properties:
    <a href="#createduration" title="CreateDuration">CreateDuration</a>: <i>String</i>
    <a href="#destroyduration" title="DestroyDuration">DestroyDuration</a>: <i>String</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - <a href="triggersdefinition.md">TriggersDefinition</a></i>
</pre>

## Properties

#### CreateDuration

[Time duration][1] to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestroyDuration

[Time duration][1] to delay resource destroy. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be successfully applied into the Terraform state before destroying this resource to take effect.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

Arbitrary map of values that, when changed, will run any creation or destroy delays again. See [the main provider documentation](../index.html) for more information.

_Required_: No

_Type_: List of <a href="triggersdefinition.md">TriggersDefinition</a>

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

