# TF::Akamai::GtmCidrmap

Use the `akamai_gtm_cidrmap` resource to create, configure, and import a GTM Classless Inter-Domain Routing (CIDR) map. CIDR mapping uses the IP addresses of the requesting name server to provide IP-specific CNAME entries. CNAMEs let you direct internal users to a specific environment or direct them to the origin. This lets you provide different responses to an internal corporate DNS infrastructure, such as internal test environments and another answer for all other name servers (`default_datacenter`).

 CIDR maps split the Internet into multiple CIDR block zones. Properties that use a map can specify a handout CNAME for each zone on the property’s editing page. To configure a property for CIDR mapping, your domain needs at least one CIDR map defined. 
 
~> **Note** Import requires an ID with this format: `existing_domain_name`:`existing_map_name`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::GtmCidrmap",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>" : <i>Boolean</i>,
        "<a href="#assignment" title="Assignment">Assignment</a>" : <i>[ <a href="assignmentdefinition.md">AssignmentDefinition</a>, ... ]</i>,
        "<a href="#defaultdatacenter" title="DefaultDatacenter">DefaultDatacenter</a>" : <i>[ <a href="defaultdatacenterdefinition.md">DefaultDatacenterDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::GtmCidrmap
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>: <i>Boolean</i>
    <a href="#assignment" title="Assignment">Assignment</a>: <i>
      - <a href="assignmentdefinition.md">AssignmentDefinition</a></i>
    <a href="#defaultdatacenter" title="DefaultDatacenter">DefaultDatacenter</a>: <i>
      - <a href="defaultdatacenterdefinition.md">DefaultDatacenterDefinition</a></i>
</pre>

## Properties

#### Domain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitOnComplete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Assignment

_Required_: No

_Type_: List of <a href="assignmentdefinition.md">AssignmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultDatacenter

_Required_: No

_Type_: List of <a href="defaultdatacenterdefinition.md">DefaultDatacenterDefinition</a>

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

