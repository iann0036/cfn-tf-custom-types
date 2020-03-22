# Terraform::Google::ComputeSharedVpcServiceProject

Enables the Google Compute Engine
[Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
feature for a project, assigning it as a Shared VPC service project associated
with a given host project.

For more information, see,
[the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
where the Shared VPC feature is referred to by its former name "XPN".

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeSharedVpcServiceProject",
    "Properties" : {
        "<a href="#hostproject" title="HostProject">HostProject</a>" : <i>String</i>,
        "<a href="#serviceproject" title="ServiceProject">ServiceProject</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeSharedVpcServiceProject
Properties:
    <a href="#hostproject" title="HostProject">HostProject</a>: <i>String</i>
    <a href="#serviceproject" title="ServiceProject">ServiceProject</a>: <i>String</i>
</pre>

## Properties

#### HostProject

The ID of a host project to associate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceProject

The ID of the project that will serve as a Shared VPC service project.

_Required_: Yes

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

