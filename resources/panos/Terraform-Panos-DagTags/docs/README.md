# Terraform::Panos::DagTags

This resource allows you to add and remove dynamic address group tags.

The `ip` field should be unique in the `panos_dag_tags` block, and there
should only be one `panos_dag_tags` block defined in a given plan.

**Note** - Tags are only removed during `terraform destroy`.  Updating an
applied terraform plan to have alternative tags will leave behind the
old tags from the previously published plan(s).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::DagTags",
    "Properties" : {
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#register" title="Register">Register</a>" : <i>[ <a href="register.md">Register</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::DagTags
Properties:
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#register" title="Register">Register</a>: <i>
      - <a href="register.md">Register</a></i>
</pre>

## Properties

#### Vsys

The vsys to put the DAG tags in (default: `vsys1`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Register

_Required_: No

_Type_: List of <a href="register.md">Register</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

