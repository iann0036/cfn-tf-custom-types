# TF::DigitalOcean::ProjectResources

Assign resources to a DigitalOcean Project. This is useful if you need to assign resources
managed in Terraform to a DigitalOcean Project managed outside of Terraform.

The following resource types can be associated with a project:

* Database Clusters
* Domains
* Droplets
* Floating IP
* Load Balancers
* Spaces Bucket
* Volume

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::ProjectResources",
    "Properties" : {
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::ProjectResources
Properties:
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
</pre>

## Properties

#### Project

the ID of the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

a list of uniform resource names (URNs) for the resources associated with the project.

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

