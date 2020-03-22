# Terraform::OCI::IdentityTagDefault

This resource provides the Tag Default resource in Oracle Cloud Infrastructure Identity service.

Creates a new tag default in the specified compartment for the specified tag definition.

If you specify that a value is required, a value is set during resource creation (either by 
the user creating the resource or another tag defualt). If no value is set, resource creation 
is blocked.

* If the `isRequired` flag is set to "true", the value is set during resource creation.
* If the `isRequired` flag is set to "false", the value you enter is set during resource creation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::IdentityTagDefault",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#isrequired" title="IsRequired">IsRequired</a>" : <i>Boolean</i>,
        "<a href="#tagdefinitionid" title="TagDefinitionId">TagDefinitionId</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::IdentityTagDefault
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#isrequired" title="IsRequired">IsRequired</a>: <i>Boolean</i>
    <a href="#tagdefinitionid" title="TagDefinitionId">TagDefinitionId</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CompartmentId

The OCID of the compartment. The tag default will be applied to all new resources created in this compartment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsRequired

(Updatable) If you specify that a value is required, a value is set during resource creation (either by  the user creating the resource or another tag defualt). If no value is set, resource  creation is blocked.
* If the `isRequired` flag is set to "true", the value is set during resource creation.
* If the `isRequired` flag is set to "false", the value you enter is set during resource creation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagDefinitionId

The OCID of the tag definition. The tag default will always assign a default value for this tag definition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

(Updatable) The default value for the tag definition. This will be applied to all new resources created in the compartment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

#### State

Returns the <code>State</code> value.

#### TagDefinitionName

Returns the <code>TagDefinitionName</code> value.

#### TagNamespaceId

Returns the <code>TagNamespaceId</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

