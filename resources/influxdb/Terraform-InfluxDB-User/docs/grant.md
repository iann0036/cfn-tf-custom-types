# Terraform::InfluxDB::User Grant

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#database" title="Database">Database</a>" : <i>String</i>,
    "<a href="#privilege" title="Privilege">Privilege</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#database" title="Database">Database</a>: <i>String</i>
<a href="#privilege" title="Privilege">Privilege</a>: <i>String</i>
</pre>

## Properties

#### Database

The name of the database the privilege is associated with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privilege

The privilege to grant (READ|WRITE|ALL).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

