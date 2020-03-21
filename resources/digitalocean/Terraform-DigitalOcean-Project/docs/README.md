# Terraform::DigitalOcean::Project

Provides a DigitalOcean Project resource.

Projects allow you to organize your resources into groups that fit the way you work.
You can group resources (like Droplets, Spaces, Load Balancers, domains, and Floating IPs)
in ways that align with the applications you host on DigitalOcean.

The following resource types can be associated with a project:

* Database Clusters
* Domains
* Droplets
* Floating IP
* Load Balancers
* Spaces Bucket
* Volume

**Note:** A Terraform managed project cannot be set as a default project.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::DigitalOcean::Project",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#purpose" title="Purpose">Purpose</a>" : <i>String</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::DigitalOcean::Project
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#environment" title="Environment">Environment</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#purpose" title="Purpose">Purpose</a>: <i>String</i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
</pre>

## Properties

#### Description

the description of the project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Purpose

the purpose of the project, (Default: "Web Application").

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

a list of uniform resource names (URNs) for the resources associated with the project.

_Required_: No

_Type_: List of String

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

Returns the <code>CreatedAt</code> value.

#### IsDefault

Returns the <code>IsDefault</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

#### OwnerUuid

Returns the <code>OwnerUuid</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

